const INPUT: &str = include_str!("inputs/day11.txt");

pub fn day11(input: &str) -> (usize, usize) {
    (input.len(), input.len())
}

fn main() {
    let (p1, p2) = day11(INPUT);
    println!("{}\n{}", p1, p2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = include_str!("inputs/day11.test1.txt");
        let (p1, p2) = day11(input);

        assert_eq!(p1, input.len());
        assert_eq!(p2, input.len());
    }

    #[test]
    fn test_main() {
        let (p1, p2) = day11(INPUT);

        assert_eq!(p1, INPUT.len());
        assert_eq!(p2, INPUT.len());
    }
}
