import java.util.Arrays;

// see question: https://leetcode.com/problems/valid-anagram/
// see solution: https://leetcode.com/problems/valid-anagram/solutions/3139922/explained-code-used-hashing-java-code/

// use HashMap<Character, Integer>
// time complexity: O(n)
// space complexity: O(1)

class ValidAnagramSolution {
    public boolean isAnagram(String s, String t) {
        // can use char ch = s.charAt(i) rather than tokenizing
        String[] tokens = s.split("");
        String[] tokent = t.split("");

        Arrays.sort(tokens);
        Arrays.sort(tokent);

        // tokens !- tokent
        return Arrays.equals(tokens, tokent);
    }
}

public class ValidAnagram {
    public static void main(String[] args) {
        String s = "anagram";
        String t = "nagaram";

        ValidAnagramSolution solution = new ValidAnagramSolution();

        boolean result = solution.isAnagram(s, t);
        System.out.println(result);
    }
}

// python solution
// class Solution:
//     def isAnagram(self, s: str, t: str) -> bool:
//         if len(s) != len(t):
//             return False

//         countS, countT = {}, {}

//         for i in range(len(s)):
//             countS[s[i]] = 1 + countS.get(s[i], 0)
//             countT[t[i]] = 1 + countT.get(t[i], 0)
//         return countS == countT

// a = dict(one=1, two=2, three=3)
// b = {'one': 1, 'two': 2, 'three': 3}
// c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
// d = dict([('two', 2), ('one', 1), ('three', 3)])
// e = dict({'three': 3, 'one': 1, 'two': 2})
// a == b == c == d == e == True
