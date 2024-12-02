const INPUT: &str = include_str!("inputs/day2.txt");

fn is_safe(report: &Vec<i32>) -> bool {
    let sign = (report[1] - report[0]).signum();        
    let mut prev = report[0];
    for num in report.iter().skip(1) {        
        let diff = num - prev;               
        if diff.signum() != sign || diff.abs() < 1 || diff.abs() > 3  {
            return false;        
        }
        prev = *num;
    }
    true
}

pub fn day2(input: &str) -> (usize, usize) {

    let mut safe = 0;
    let mut safed = 0;
    for line in input.lines() {
        let nums = line
            .split_whitespace()
            .map(|n| n.parse::<i32>().unwrap())
            .collect::<Vec<_>>();
           
        if is_safe(&nums) { safe += 1; }
        for i in 0..nums.len() {
            
            let mut n = nums.clone();
            n.remove(i);                        
            if is_safe(&n) {                 
                safed += 1; 
                break;
            }
        }        
    }

    
    (safe as usize, safed as usize)
}

fn main() {
    let (p1, p2) = day2(INPUT);
    println!("{}\n{}", p1, p2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = include_str!("inputs/day2.test1.txt");
        let (p1, p2) = day2(input);

        assert_eq!(p1, 2);
        assert_eq!(p2, 4);
    }

    #[test]
    fn test_main() {
        let (p1, p2) = day2(INPUT);

        assert_eq!(p1, 242);
        assert_eq!(p2, 311);
    }
}
