String cout_sort(string str){
  // need to store the frequency
  vector<int> freq(26,0);
  for(int i=0;i<str.length;i++){
    int index =str[i]-'a';
    freq[index]++;
  }

  // sort the string
  int j=0;
  for(int i=0;i<26;i++){
    while(str[i]--){
      str[j++]=i+'a';
    }
  }
  return str;
}
