class PlusOneSolution {
    public int[] plusOne(int[] digits) {
        int id = digits.length-1;
        int arr[];

        while (id >= 0) {
            if (digits[id] == 9) {
                digits[id] = 0;
                id--;
            } else {
                digits[id] += 1;
                break;
            }
        }

        if (id < 0) {
            arr = new int[digits.length + 1];
            arr[0] = 1;
            for (int i = 0; i < digits.length-1; i++) {
                arr[i+1] = digits[i];
            }
        } else {
            arr = digits;
        }

        return arr;
    }
}

public class PlusOne {
    public static void main(String[] args) {
        int[] arr = {9,9,9};

        PlusOneSolution solution = new PlusOneSolution();
        int[] newArr = solution.plusOne(arr);

        for (int num : newArr) {
            System.out.println(num);
        }
    }
}
