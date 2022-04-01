use std::collections::HashMap;

fn is_prime(is_prime_map: &mut HashMap<i32, bool>, x: i32) -> bool {
    match is_prime_map.get(&x) {
        Some(&v) => v,
        None => {
            // println!("missed cache!");
            let result = match x {
                2 => true,
                v if v < 2 => false,
                _ => {
                    let mut r = true;
                    for i in 2..=((x as f64).sqrt() as i32) {
                        if is_prime(is_prime_map, i) && x % i == 0 {
                            r = false;
                            break;
                        }
                    }
                    r
                }
            };
            is_prime_map.insert(x, result);
            result
        }
    }
}

fn find_product(max_bound: i32) -> i32 {
    let mut is_prime_map = HashMap::<i32, bool>::new();
    let mut highest = 0;
    let mut product = 0;
    for a in (-1 * (max_bound - 1))..max_bound {
        for b in (-1 * max_bound)..=max_bound {
            // println!("a {} b {}", a, b);
            let num_primes = (0..)
                .map(|x| (x as i32).pow(2) + a * x + b)
                .take_while(|x| is_prime(&mut is_prime_map, *x))
                .count();

            if num_primes > highest {
                highest = num_primes;
                product = a * b;
            }
        }
    }
    product
}

fn main() {
    println!("Hello, world! {}", find_product(1000));
}

#[cfg(test)]
mod tests {
    use super::find_product;
    use super::is_prime;
    use std::collections::HashMap;

    #[test]
    fn test_is_prime() {
        let mut is_prime_map = HashMap::<i32, bool>::new();
        assert_eq!(is_prime(&mut is_prime_map, 2), true);
        assert_eq!(is_prime(&mut is_prime_map, 3), true);
        assert_eq!(is_prime(&mut is_prime_map, 4), false);
    }

    #[test]
    fn test_find_product() {
        assert_eq!(find_product(0), 0);
        assert_eq!(find_product(1), 0);
    }
}
