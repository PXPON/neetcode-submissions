use std::collections::HashMap;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        // Create a hash table
        let mut map = HashMap::new();

        for num in nums {
            if map.contains_key(&num) {
                return true;
            }
            else {
                map.insert(num, 1);
            }
        }

        return false;
    }
}
