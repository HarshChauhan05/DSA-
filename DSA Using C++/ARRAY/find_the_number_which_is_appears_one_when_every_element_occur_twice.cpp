int getSingleElement(vector<int> &arr) {
    int n = arr.size();
    // XOR all the elements:
    int xorr = 0;
    for (int i = 0; i < n; i++) {  // xor of two same number  is zero. A^A =0 || A^0=A
        xorr = xorr ^ arr[i];
    }
    return xorr;
}


this can be solve by Hashing. 
try yourself. 
