const INPUT: &str = include_str!("inputs/day7.txt");

fn runops( nums: &[usize], inx: usize, target: usize, acc: usize, do2: bool) -> bool {
    if acc > target {
        return false;
    }
    if inx == nums.len() {
        return acc == target;        
    }

    if runops(nums, inx + 1, target, acc * nums[inx], do2 ) {
        return true;
    }

    if runops(nums, inx + 1, target, acc + nums[inx], do2 ) {
        return true;
    }
    if do2 {
        let new_acc:usize = (acc.to_string() + &nums[inx].to_string())
            .parse()
            .unwrap();

        if runops(nums, inx + 1, target, new_acc, do2) {
            return true;
        }
    }

    false
}

fn day7(input: &str) -> (usize, usize) {
    let mut r1 = 0;
    let mut r2 = 0;
    for line in input.lines() {
        let (target,numstr) = line
            .split_once(":")
            .map(|(f,s)| (f.parse::<usize>().unwrap(), s) )
            .unwrap();
        let nums = numstr
            .split_whitespace()
            .map(|x| x.parse::<usize>().unwrap())
            .collect::<Vec<_>>();

        if runops(&nums, 1, target, nums[0], false ) {
            r1 += target;
        }
        if runops(&nums, 1, target, nums[0], true ) {
            r2 += target;
        }
    }
    
    (r1, r2)
}

fn main() {
    let (p1, p2) = day7(INPUT);
    println!("{}\n{}", p1, p2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = include_str!("inputs/day7.test1.txt");
        let (p1, p2) = day7(input);

        assert_eq!(p1, 3749);
        assert_eq!(p2, 11387);
    }

    #[test]
    fn test_main() {
        let (p1, p2) = day7(INPUT);

        assert_eq!(p1, 12940396350192);
        assert_eq!(p2, 106016735664498);
    }
}
