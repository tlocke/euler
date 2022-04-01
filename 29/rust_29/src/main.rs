use std::collections::HashSet;

fn add(a: &Vec<usize>, b: &Vec<usize>) -> Vec<usize> {
    // println!("add a {:?} b {:?}", a, b);
    let mut r: Vec<usize> = Vec::from_iter(a.iter().map(|x| *x));

    for _ in r.len()..b.len() {
        r.push(0);
    }
    r.push(0);

    let mut carry = 0;

    for i in 0..r.len() {
        let s = b.get(i).unwrap_or(&0) + r[i] + carry;

        match s > 9 {
            true => {
                r[i] = s - 10;
                carry = 1;
            }
            false => {
                r[i] = s;
                carry = 0;
            }
        }
    }

    if *r.last().unwrap() == 0 {
        r.pop();
    }
    r
}

fn mult(a: &Vec<usize>, b: &Vec<usize>) -> Vec<usize> {
    // println!("mult a {:?} b {:?}", a, b);
    let mut r: Vec<usize> = vec![0];

    for (i, d) in b.iter().enumerate() {
        for _ in 0..*d {
            let mut to_add = vec![0; i];
            to_add.extend(a.iter());
            r = add(&r, &to_add);
        }
    }
    r
}
fn pwr(a: &Vec<usize>, b: usize) -> Vec<usize> {
    match b {
        0 => vec![1],
        _ => {
            let mut r: Vec<usize> = add(&vec![0], a);

            for _ in 0..(b - 1) {
                r = mult(&r, a);
            }
            r
        }
    }
}

fn distinct_powers(max: usize) -> usize {
    let mut pwrs: HashSet<Vec<usize>> = HashSet::new();
    let mut a: Vec<usize> = vec![1];
    for _ in 2..=max {
        a = add(&a, &vec![1]);
        for b in 2..=max {
            println!("distinct_powers a {:?} b {}", a, b);
            pwrs.insert(pwr(&a, b));
        }
    }

    pwrs.len()
}

fn run(max: usize) {
    println!("max {} num_distinct {}", max, distinct_powers(max));
}

fn main() {
    run(5);
    run(100);
}

#[cfg(test)]
mod tests {
    use super::add;
    use super::mult;
    use super::pwr;

    #[test]
    fn test_add() {
        let a = vec![1, 1];
        let b = vec![1];
        assert_eq!(add(&a, &b), vec![2, 1]);
    }

    #[test]
    fn test_add_carry() {
        let a = vec![8];
        let b = vec![8];
        assert_eq!(add(&a, &b), vec![6, 1]);
    }

    #[test]
    fn test_add_10() {
        let a = vec![8];
        let b = vec![2];
        assert_eq!(add(&a, &b), vec![0, 1]);
    }

    #[test]
    fn test_add_carry_carry() {
        let a = vec![9, 9];
        let b = vec![1];
        assert_eq!(add(&a, &b), vec![0, 0, 1]);
    }

    #[test]
    fn test_pwd() {
        let a = vec![1];
        let b = 1;
        assert_eq!(pwr(&a, b), vec![1]);
    }

    #[test]
    fn test_mult() {
        let a = vec![8];
        let b = vec![2];
        assert_eq!(mult(&a, &b), vec![6, 1]);
    }
}
