use std::collections::HashSet;

const INPUT: &str = include_str!("inputs/day6.txt");

fn walkpos( p:(usize,usize), d: usize) -> (usize, usize) {
    let dirs = [(0,-1), (1,0), (0,1), (-1,0)];
    let (dc, dr) = dirs[d];
    let (rr, cc) = (p.0 as isize + dr, p.1 as isize + dc);
    (rr as usize, cc as usize)
}

fn walk(map: &Vec<Vec<u8>>, mut pos: (usize, usize)) -> (HashSet<(usize,usize)>, bool) {
    let mut seen = HashSet::new();    
    let mut dir = 0;
    loop {
        if seen.contains(&(pos.0,pos.1,dir)) {
            return (HashSet::new(), true);
        }        
        seen.insert((pos.0, pos.1, dir));

        let npos = walkpos(pos, dir);

        if let Some(c) = map.get(npos.0).and_then(|x| x.get(npos.1)) {
            if *c == b'#' {
                dir = (dir + 1) % 4;
            } else {
                pos = npos;
            }            
        } else {
            return (seen.iter().map(|(r,c,_)| (*r,*c) ).collect(), false);
        }
    }
}

fn day6(input: &str) -> (usize, usize) {
    let mut map = input.lines().map(|x| x.as_bytes().to_vec()).collect::<Vec<_>>();
    let size = (map.len(), map[0].len());
    let mut pos = (0,0);
    for r in 0..size.0 {
        for c in 0..size.1 {
           if map[r][c]  == b'^' {
                map[r][c] = b'.';
                pos = (r,c);
            }        
        }
    }

    let (visited,_) = walk(&map, pos);
    let visits = visited.len();

    let mut loops = 0;
    for obs in visited {
        map[obs.0][obs.1] = b'#';
        let (_,looped) = walk(&map, pos);
        if looped {
            loops += 1;
        }
        map[obs.0][obs.1] = b'.';
    }

    (visits, loops)
}

fn main() {
    let (p1, p2) = day6(INPUT);
    println!("{}\n{}", p1, p2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = include_str!("inputs/day6.test1.txt");
        let (p1, p2) = day6(input);

        assert_eq!(p1, 41);
        assert_eq!(p2, 6);
    }

    #[test]
    fn test_main() {
        let (p1, p2) = day6(INPUT);

        assert_eq!(p1, 4988);
        assert_eq!(p2, 1697);
    }
}
