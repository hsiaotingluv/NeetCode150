class CountBoundedSlicesSolution {
    public int solution(int K, int[] A) {
        int len = A.length;
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        int count = 0;

        for (int i = 0; i < len; i++) {
            for (int j = i; j < len; j++) {
                int first = A[i];
                int second = A[j];

                if (Math.max(first, second) > max) {
                    max = Math.max(first, second);
                }
                if (Math.min(first, second) < min) {
                    min = Math.min(first, second);
                }

                if (max - min <= K) {
                    count += 1;
                } else {
                    break;
                }
            }
            max = Integer.MIN_VALUE;
            min = Integer.MAX_VALUE;
        }

        return count > 1000000000 ? 1000000000 : count;
    }
}

public class CountBoundedSlices {
    public static void main(String[] args) {
        int[] arr = {3, 5, 7, 6, 3};
        CountBoundedSlicesSolution sol = new CountBoundedSlicesSolution();

        int result = sol.solution(2, arr);
        System.out.println(result);

        int a = 'a';
        System.out.println(a++);
    }
}

