fn equal(x: u32, p: u32) -> bool {
    x == x
        .to_string()
        .chars()
        .map(|y| y.to_digit(10).unwrap().pow(p))
        .sum()
}

fn pwrs(p: u32) -> u32 {
    let m = 9_u32.pow(p);
    let max = (2..).skip_while(|x| 10_u32.pow(*x) < x * m).next().unwrap() * m;
    println!("max {}", max);
    (2..=max).filter(|x| equal(*x, p)).sum()
}

fn run(p: u32) {
    println!("p {} pwrs {}", p, pwrs(p));
}

fn main() {
    run(4);
    run(5);
}
