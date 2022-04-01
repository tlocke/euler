use std::collections::BTreeMap;
use std::collections::HashMap;
use std::collections::HashSet;

fn num_distinct(max: usize) -> usize {
    let mut pfs: HashMap<usize, BTreeMap<usize, usize>> = HashMap::new();
    let mut primes: Vec<usize> = vec![];
    let mut distinct: HashSet<BTreeMap<usize, usize>> = HashSet::new();

    for a in 2..=max {
        let pf: BTreeMap<usize, usize> = match primes.iter().skip_while(|x| a % **x > 0).next() {
            Some(p) => {
                let mut f: BTreeMap<usize, usize> = pfs[&(a / p)].to_owned();
                f.insert(*p, f.get(p).unwrap_or(&0) + 1);
                f
            }
            None => {
                primes.push(a);
                BTreeMap::from([(a, 1)])
            }
        };
        for b in 2..=max {
            distinct.insert(pf.iter().map(|(k, v)| (*k, v * b)).collect());
        }
        pfs.insert(a, pf);
    }
    distinct.len()
}

fn run(max: usize) {
    println!("max {} num_distinct {}", max, num_distinct(max));
}
fn main() {
    run(5);
    run(100);
}

#[cfg(test)]
mod tests {
    use super::num_distinct;

    #[test]
    fn test_num_distinct() {
        assert_eq!(num_distinct(5), 15);
    }
}
