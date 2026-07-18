class Solution {
public:
    int reverse(int x) {
        int r;
        long long y=x;
       long long l=0;
        if (y<0)
        y=y*-1;
        while(y>0){
            r=y%10;
            l=l*10+r;
            y=y/10;
        }
        
        
            
            if (l>=INT_MIN and l<=INT_MAX){
                if (x<0){
                    return -1*l;
                }else{
                    return l;
                }
            }
            else{
                return 0;
            }
        
    }
};