fn combos(dens: &[usize], tot: usize) -> usize {
    if tot == 200 {
        return 1;
    }

    if dens.len() == 0 {
        return 0;
    }

    let ndens = &dens[1..];
    (tot..=200)
        .step_by(dens[0])
        .map(|x| combos(&ndens, x))
        .sum()
}

fn main() {
    let denoms: Vec<usize> = vec![200, 100, 50, 20, 10, 5, 2, 1];
    println!("{}", combos(&denoms, 0));
}
