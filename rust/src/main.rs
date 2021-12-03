use std::fs;

fn main() {
    print!("Day2-1 ");
    day2_1()
}

fn day2_1() {
    println!(
        "{:?}",
        fs::read_to_string("../day2.txt")
            .unwrap()
            .lines()
            .fold([0, 0], |mut acc, line| {
                match line.split_once(" ").unwrap() {
                    ("forward", step) => {
                        acc[0] += step.parse::<i32>().unwrap();
                        acc
                    }
                    ("down", step) => {
                        acc[1] += step.parse::<i32>().unwrap();
                        acc
                    }
                    ("up", step) => {
                        acc[1] -= step.parse::<i32>().unwrap();
                        acc
                    }
                    _ => acc,
                }
            },)
            .iter()
            .product::<i32>()
    );
}
