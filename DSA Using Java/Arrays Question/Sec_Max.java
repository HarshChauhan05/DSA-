class Second_Max_Element {
    public static void main(String[] args) {
        System.out.println("Second Maximun Element in the array");
        int arr[] = {1,6,2,9,6,12};
        int n=arr.length;
        int max = Integer.MIN_VALUE;
        for(int i=0;i<n;i++){
            if(max<arr[i]){
                max=arr[i];
            }
            
            }
            int Sec_Max = Integer.MIN_VALUE;
            for(int i=0;i<n;i++){
                if(Sec_Max<arr[i] && arr[i]<max){
                    Sec_Max =arr[i];
                }
                }
                System.out.println(Sec_Max);
}
}