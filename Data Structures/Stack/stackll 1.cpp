#include <iostream>
#include<string>
#include <sstream>
using namespace std;

template<class E>
class StackLL {
private:
	
	E *stack;

public:
	StackLL(){
		
		
	}
	int size(){

	}

	bool isEmpty(){
		return(size() == 0)
	}

	void push(E& elt){

	}

	E pop(){

	}

	E top(){
		
	}
	void printstack(){
		if isEmpty(){
			cout<< "Empty";
		}
		else{
			
			cout << endl;
			return;
		}
	}
};

int getValue(string s, int pos) {
    istringstream iss(s);
    string temp;
    iss>>temp;
    iss>>temp;
    if(pos==1) {
        return stoi(temp);
    }
    else {
        iss>>temp;
        return stoi(temp);
    }
}
//Driver Code
int main(){
	string noOfInputs,str;
 	StackLL<int> stack1();
 	getline(cin, noOfInputs);
 	for(int i=0;i<stoi(noOfInputs);i++){
 	    getline(cin, str); 
 	    
 	    if (str.substr(0, 1) == "S"){
 	       cout<< stack1.size()<<endl;
 	    }
 	    else if (str.substr(0,1) == "I"){
 	        //cout<<slist1.isEmpty()<<endl;
 	        if(stack1.isEmpty()){
 	            cout<<"True"<<endl;
 	        }
 	        else{
 	            cout<<"False"<<endl;
 	        }
 	    }
 	    else if (str.substr(0, 1) == "P"){
 	        int value = getValue(str, 1);
 	        stack1.push(value);
 	        stack1.printstack();
 	    }
 	    else if (str.substr(0, 1) == "O"){
 	        cout << stack1.pop;
 	        stack1.printstack();
 	    }
 	    else if (str.substr(0, 1) == "T"){
 	        cout << stack1.pop;
 	        stack1.printstack();
 	    }
 	    
 	}
}