use regex::Regex;

const INPUT: &str = include_str!("inputs/day3.txt");

pub fn day3(input: &str) -> (usize, usize) {
    let regex = Regex::new(r"mul\((\d\d?\d?),(\d\d?\d?)\)").unwrap();

    let mut acc = 0;
    for (_, [num1, num2]) in regex.captures_iter(input).map(|c| c.extract()) {
        acc += num1.parse::<i32>().unwrap() * num2.parse::<i32>().unwrap();
        
    }
    (acc as usize, input.len())
}

fn main() {
    let input = include_str!("inputs/day3.test2.txt");
    let (p1, p2) = day3(input);
    
    // let (p1, p2) = day3(INPUT);
    // println!("{}\n{}", p1, p2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = include_str!("inputs/day3.test1.txt");
        let (p1, p2) = day3(input);

        assert_eq!(p1, 161);
        assert_eq!(p2, input.len());
    }

    #[test]
    fn test2() {
        let input = include_str!("inputs/day3.test2.txt");
        let (p1, p2) = day3(input);

        assert_eq!(p1, 161);
        assert_eq!(p2, input.len());
    }


    // //#[test]
    // fn test_main() {
    //     let (p1, p2) = day3(INPUT);

    //     assert_eq!(p1, 170778545);
    //     assert_eq!(p2, INPUT.len());
    // }
}
