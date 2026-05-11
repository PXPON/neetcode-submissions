impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        // Turn each into letter arrays and sort them
        // let mut s_chars: Vec<char> = s.chars().collect();
        let mut s_chars: Vec<char> = s.chars().collect();
        let mut t_chars: Vec<char> = t.chars().collect();

        s_chars.sort();
        t_chars.sort();

        if s_chars == t_chars { return true; }
        return false;
    }
}
