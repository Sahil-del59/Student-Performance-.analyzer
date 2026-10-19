import numpy as np
def analyze_performance(filename):
    try:
        f=np.loadtxt("scores.txt") #load file to f
        student_id=f[:,0]
        student_marks=f[:,1:]

        print("...class performance...")
        #mean marks per subject(column wise)
        mean_score_per_sub=np.mean(student_marks,axis=0)
        print("average score per subject:",mean_score_per_sub)\
        #highest and lowest marks in class
        print("highest marks in class:",np.max(student_marks))
        print("minimun marks in class:",np.min(student_marks))
        #indivisual mean marks of each student
        scores=np.mean(student_marks,axis=1)
        for id,marks in zip(student_id,scores):
            print(f"student id:{id} average marks: {marks:.2f}")
    except:
        print("FileNotFoundError")
if __name__=="__main__":
   analyze_performance("scores.txt")
