use std::collections::HashMap;

const INPUT: &str = include_str!("inputs/day1.txt");

pub fn day1(input: &str) -> (usize, usize) {

    let mut left = Vec::new();
    let mut right = Vec::new();
    let mut counts:HashMap<i32,i32> = HashMap::new();
    for line in input.lines() {
        let nums = line
            .split_whitespace()
            .map(|n| n.parse::<i32>().unwrap())
            .collect::<Vec<_>>();
        left.push(nums[0]);
        right.push(nums[1]);
        *counts.entry(nums[1]).or_insert(0) += 1;
    }
    left.sort();
    right.sort();

    let nums = left.iter().zip(right.iter());
    let mut distance: i32 = 0;
    let mut similarity: i32 = 0;
    for (lnum, rnum) in nums {
        distance += (lnum - rnum).abs();
        similarity += lnum * counts.get(lnum).unwrap_or(&0);
    }

    (distance as usize, similarity as usize)
}

fn main() {
    let (p1, p2) = day1(INPUT);
    println!("{}\n{}", p1, p2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = include_str!("inputs/day1.test1.txt");
        let (p1, p2) = day1(input);

        assert_eq!(p1, 11);
        assert_eq!(p2, 31);
    }

    #[test]
    fn test_main() {
        let (p1, p2) = day1(INPUT);

        assert_eq!(p1, 1197984);
        assert_eq!(p2, 23387399);
    }
}
