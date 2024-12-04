const INPUT: &str = include_str!("inputs/day4.txt");

fn run_search(ws: &Vec<Vec<char>>, x:i32, y:i32, dx:i32, dy:i32, n: char ) -> bool {
    let x =  x + dx;
    let y = y + dy;
    // Argh - casting to usize all the time!!
    if x < 0 || y < 0 || (x as usize) >= ws[0].len() || (y as usize) >= ws.len() {
        return false;
    }
    if ws[y as usize][x as usize] == n {
        if n == 'S' {
            return true;
        } else if n == 'M' {
            return run_search(&ws, x, y, dx, dy, 'A');
        } else if n == 'A' {
            return run_search(&ws, x, y, dx, dy, 'S');
        } else {
            // Not sure why Rust insists I have this...
            panic!("wrong");
        }
    } else {
        return false;
    }
}

fn run_search2(ws: &Vec<Vec<char>>, x:i32, y:i32 ) -> bool {
    if x < 1 || y < 1 || (x as usize) >= ws[0].len()-1 || (y as usize) >= ws.len()-1 {
        return false;
    }

    let mut found = 0;
    for (dx,dy,dx2,dy2) in [(1, 1,-1,-1), (-1, 1, 1, -1)] {
        let x1 =  (x + dx) as usize;
        let y1 = (y + dy) as usize;
        let x2 =  (x + dx2) as usize;
        let y2 = (y + dy2) as usize;
        if (ws[y1][x1] == 'M' && ws[y2][x2] == 'S') || (ws[y1][x1] == 'S' && ws[y2][x2] == 'M')
        {
            found += 1;
        }
    }

    found == 2
}

pub fn day4(input: &str) -> (usize, usize) {

    let lines:Vec<&str> = input.lines().collect();
    let mut ws:Vec<Vec<char>> = Vec::new();
    // Sure there must be a more idiomatic way of doing this next bit
    for line in lines {
        ws.push(line.chars().collect());
    }

    let mut acc = 0;
    let mut acc2 = 0;
    for y in 0..ws.len() {
        for x in 0..ws[0].len() {
            if ws[y][x] == 'X' {
                for (dx,dy) in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)] {
                    if run_search(&ws, x as i32, y as i32, dx, dy, 'M') {
                        acc += 1;
                    }
                }
            }
            if ws[y][x] == 'A' {
                if run_search2(&ws, x as i32, y as i32) {
                    acc2 += 1;
                }
            }
        }
    }

    (acc, acc2)
}

fn main() {
    let (p1, p2) = day4(INPUT);
    println!("{}\n{}", p1, p2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = include_str!("inputs/day4.test1.txt");
        let (p1, p2) = day4(input);

        assert_eq!(p1, 18);
        assert_eq!(p2, 9);
    }

    #[test]
    fn test_main() {
        let (p1, p2) = day4(INPUT);

        assert_eq!(p1, 2532);
        assert_eq!(p2, 1941);
    }
}
