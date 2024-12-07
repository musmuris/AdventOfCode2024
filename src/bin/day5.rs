use std::cmp::Ordering;
use std::collections::HashMap;
use std::collections::HashSet;

const INPUT: &str = include_str!("inputs/day5.txt");

pub fn day5(input: &str) -> (usize, usize) {

    let mut rules = HashMap::<u32,(HashSet::<u32>,HashSet::<u32>)>::new();
    let mut i = input.lines();
    loop {
        let line = i.next().unwrap();
        if line.len() == 0 {
            break;
        }
        let Some((first,second)) = line.split_once("|") else {panic!("No !?")};
        //after
        let set = rules.entry(first.parse::<u32>().unwrap()).or_default();
        set.0.insert(second.parse::<u32>().unwrap());
        // before
        let set = rules.entry(second.parse::<u32>().unwrap()).or_default();
        set.1.insert(first.parse::<u32>().unwrap());

    }

    let mut sum = 0;
    let mut sum2 = 0;
    for line in i {
        let update = line.split(",").map(|x| x.parse::<u32>().unwrap()).collect::<Vec<_>>();
        let mut sorted = update.clone();
        sorted.sort_by(|a,b| {
            if rules[a].1.contains(b) {
                Ordering::Greater
            } else {
                Ordering::Less
            }
        });

        if update.iter().zip(sorted.iter()).all(|(a,b)| a == b) {
            // get middle
            sum += update[update.len()/2];
        } else {
            sum2 += sorted[sorted.len()/2];
        }
    }

    (sum as usize, sum2 as usize)
}

fn main() {
    let (p1, p2) = day5(INPUT);
    println!("{}\n{}", p1, p2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = include_str!("inputs/day5.test1.txt");
        let (p1, p2) = day5(input);

        assert_eq!(p1, 143);
        assert_eq!(p2, 123);
    }

    #[test]
    fn test_main() {
        let (p1, p2) = day5(INPUT);

        assert_eq!(p1, 4135);
        assert_eq!(p2, 5285);
    }
}
