fn diag_side(side: usize) -> usize {
    let start = (side - 2).pow(2) + side - 1;
    (start..).step_by(side - 1).take(4).sum::<usize>()
}

fn diag_sum(side: usize) -> usize {
    (3..=side).step_by(2).map(diag_side).sum::<usize>() + 1
}

fn main() {
    println!("side {} diag_sum {}", 1, diag_sum(1));
    println!("side {} diag_sum {}", 3, diag_sum(3));
    println!("side {} diag_sum {}", 1001, diag_sum(1001));
}
