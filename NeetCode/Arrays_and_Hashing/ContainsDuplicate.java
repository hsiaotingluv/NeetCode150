import java.util.Hashtable;

// see question: https://leetcode.com/problems/contains-duplicate/
// see solution: https://leetcode.com/problems/contains-duplicate/solutions/3163705/java-best-solution-3-ways/

// time complexity: O(n)
// space complexity: O(n)
class ContainsDuplicateSolution {
    public boolean containsDuplicate(int[] nums) {
        // can use HashMap instead, run faster than hashtable
        // HashMap vs HashTable vs HashSet: https://www.golinuxcloud.com/hashmap-vs-hashtable-vs-hashset-in-java/#:~:text=The%20HashMap%20class%20extends%20the,Serializable%2C%20Cloneable%20and%20Set%20interface.
        Hashtable<Integer, Boolean> hashtable = new Hashtable<Integer, Boolean>();
        boolean hasDuplicate = false;

        for (int i = 0; i < nums.length; i++) {
            if (hashtable.containsKey(nums[i])) {
                hasDuplicate = true;
                break;
            } else {
                hashtable.put(nums[i], true);
            }
        }
        return hasDuplicate;
    }
}

public class ContainsDuplicate {
    public static void main(String[] args) {
        int[] input = {1,2,3,1};

        ContainsDuplicateSolution solution = new ContainsDuplicateSolution();

        boolean result = solution.containsDuplicate(input);

        System.out.println(result);
    }
}

// python solution
// class Solution:
//     def containsDuplicate(self, nums: list[int]) -> bool:
//         hashset = set()

//         for n in nums:
//             if n in hashset:
//                 return True
//             hashset.add(n)
//         return False

