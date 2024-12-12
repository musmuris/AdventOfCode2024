use itertools::Itertools;
use std::collections::{HashMap, HashSet};

const INPUT: &str = include_str!("inputs/day8.txt");


fn find_ants(map: &[&[u8]]) -> HashMap<u8, Vec<(usize,usize)>> {
    let mut ants = HashMap::<u8, Vec<_>>::new();
    for r in 0..map.len() {
        for c in 0..map[0].len() {
            if map[r][c] != b'.' {
                ants.entry(map[r][c]).or_default().push((r,c));
            }
        }
    }
    ants
}

fn find_pair_nodes( nodes: &mut HashSet<(usize,usize)>,
                    harmonic_nodes: &mut HashSet<(usize,usize)>,
                    r:usize, c:usize, dr:isize, dc:isize) {
    let mut d = 0;
    loop {
        let nr = r+(dr*d);
        let nc = c+(dc*d);
        if !((0..self.height).contains(&nr) && (0..).contains(&nc)) {
            break
        }
        harmonic_nodes.insert((nr,nc));
        if d == 1 {
            nodes.insert((nr,nc));      
        }
        d += 1;
    }
}

fn find_nodes(map: &[&[u8]], ants: &HashMap<u8, Vec<(usize,usize)>>) {
    let mut nodes: HashSet<(usize,usize)> = HashSet::new();
    let mut harmonic_nodes: HashSet<(usize,usize)> = HashSet::new();
    for (_,v) in ants.iter() {
        for pairs in v.iter().combinations(2) {
            let(r1,c1) = *pairs[0];
            let(r2,c2) = *pairs[1];
            let dr = (r1-r2) as isize;
            let dc = (c1-c2) as isize;

            //find_pair_nodes(&mut nodes, &mut harmonic_nodes, r1, c1, dr, dc);
            //find_pair_nodes(&mut nodes, &mut harmonic_nodes, r2, c2, 0-dr, 0-dc);
        }
    }
}


fn day8(input: &str) -> (usize, usize) {
    let map = input.lines().map(|x| x.as_bytes()).collect::<Vec<_>>();

    let ants = find_ants(&map);
    find_nodes(&map, &ants);

    (input.len(), input.len())
}

fn main() {
    let (p1, p2) = day8(INPUT);
    println!("{}\n{}", p1, p2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let input = include_str!("inputs/day8.test1.txt");
        let (p1, p2) = day8(input);

        assert_eq!(p1, 14);
        assert_eq!(p2, 34);
    }

    #[test]
    fn test_main() {
        let (p1, p2) = day8(INPUT);

        assert_eq!(p1, 276);
        assert_eq!(p2, 991);
    }
}
