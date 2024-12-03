use regex::Regex;

const INPUT: &str = include_str!("inputs/day3.txt");

pub fn day3(input: &str) -> (usize, usize) {
    let regex = Regex::new(r"(do\(\)|(don't\(\)))|mul\((\d\d?\d?),(\d\d?\d?)\)").unwrap();

    let mut acc1 = 0;
    let mut acc2 = 0;
    let mut doit = true;
    for a in regex.captures_iter(input) {
        if &a[0] == "do()" {
            doit = true;
        } else if &a[0] == "don't()" {
            doit = false;
        }
        else {
            let m = &a[3].parse::<i32>().unwrap() * &a[4].parse::<i32>().unwrap();
            acc1 += m;
            if doit {
                acc2 += m;
            }
        }     
    }
    (acc1 as usize, acc2 as usize)
}

fn main() {        
    let (p1, p2) = day3(INPUT);
    println!("{}\n{}", p1, p2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = include_str!("inputs/day3.test1.txt");
        let (p1, p2) = day3(input);

        assert_eq!(p1, 161);
        assert_eq!(p2, 161);
    }

    #[test]
    fn test2() {
        let input = include_str!("inputs/day3.test2.txt");
        let (p1, p2) = day3(input);

        assert_eq!(p1, 161);
        assert_eq!(p2, 48);
    }


    #[test]
    fn test_main() {
        let (p1, p2) = day3(INPUT);

        assert_eq!(p1, 170778545);
        assert_eq!(p2, 82868252);
    }
}
