100  DIM C(50) 
110  S=10
111  NSTOP=10000         
120  FOR D=1 TO NSTOP       
130  IA= -1/4 * LOG(1 - Rnd())
140  A=A+IA                
150  J=0 
160  J=J+1  
170  IF J=S+1 THEN K=K+1  
180  IF J=S+1 THEN 270 
190  IF A<C(J) THEN 160  
200  X=2.4  
210  C(J)=A+X 
220  M=C(1) 
230  FOR I=2 TO S 
240  IF C(I)<M THEN M=C(I) 
250  NEXT I 
260  IF M>A THEN AB=AB+M-A 
270  NEXT D 
280  PRINT K/NSTOP,AB/A
system