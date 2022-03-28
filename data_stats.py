import pandas as pd 
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import csv 
import statistics 

def setup():
     # importing data from the CSV file 
 df = pd.read_csv('std_data.csv')

 #sorting data 
 UndergradStudent_df = df.loc[df['level of education'] == "bachelor's degree"]
 HighSchoolStudent_df = df.loc[df['level of education'] == "high school"]
 PGStudent_df = df.loc[df['level of education'] == "master's degree"]
  
 stat_data = df['math score'].to_list()
 data = PGStudent_df['math score'].to_list()
 data1 = HighSchoolStudent_df['math score'].to_list()
 data2 = UndergradStudent_df['math score'].to_list()

 #Finding mean of sorted data
 Mean_PGStudent = statistics.mean(data)
 Mean_HighSchoolStudent = statistics.mean(data1)
 Mean_UGStudent = statistics.mean(data2)
 

 median_PGStudent = statistics.median(data)
 median_HighSchoolStudent = statistics.median(data1)
 median_UGStudent = statistics.median(data2)

 mode_PGStudent = statistics.mode(data)
 mode_HighSchoolStudent = statistics.mode(data1)
 mode_UGStudent = statistics.mode(data2)

 std_PGStudent = statistics.stdev(data)
 std_HighSchoolStudent = statistics.stdev(data1)
 std_UGStudent = statistics.stdev(data2)


 first_std_PG_start, first_std_PG_end = Mean_PGStudent - std_PGStudent, Mean_PGStudent + std_PGStudent
 second_std_PG_start, second_std_PG_end = Mean_PGStudent - (2*std_PGStudent), Mean_PGStudent + (2*std_PGStudent)
 third_std_PG_start, third_std_PG_end = Mean_PGStudent - (3*std_PGStudent), Mean_PGStudent + (3*std_PGStudent)
 data_within_first_std = [result for result in data if result > first_std_PG_start and result < first_std_PG_end ]
 data_within_second_std = [result for result in data if result > second_std_PG_start and result < second_std_PG_end]
 data_within_third_std = [result for result in data if result > third_std_PG_start  and result < third_std_PG_end]


 first_std_HG_start, first_std_HG_end = Mean_HighSchoolStudent - std_HighSchoolStudent, Mean_HighSchoolStudent + std_HighSchoolStudent
 second_std_HG_start, second_std_HG_end = Mean_HighSchoolStudent - (2*std_HighSchoolStudent), Mean_HighSchoolStudent + (2*std_HighSchoolStudent)
 third_std_HG_start, third_std_HG_end = Mean_HighSchoolStudent - (3*std_HighSchoolStudent), Mean_HighSchoolStudent + (3*std_HighSchoolStudent)
 data1_within_first_std = [result for result in data if result > first_std_HG_start and result < first_std_HG_end ]
 data1_within_second_std = [result for result in data if result > second_std_HG_start and result < second_std_HG_end]
 data1_within_third_std = [result for result in data if result > third_std_HG_start  and result < third_std_HG_end]

 def show_dataStats():
       
  #printing data statistics
  print('Mean score of PG Student in maths is ' + str(Mean_HighSchoolStudent))
  print('Mean score of high school  Student in maths is ' + str(Mean_HighSchoolStudent))
  print('Mean score of UG Student in maths is ' + str(Mean_UGStudent))
  
  print('Median of PG students math score is ' + str(median_PGStudent))
  print('Median of high school students maths score is ' + str(median_HighSchoolStudent))
  print('Median of UG Students maths score is ' + str(median_UGStudent))
  
  print("Mode of the PG students math score is " + str(mode_PGStudent))
  print("Mode of High school students math score is "+ str(mode_HighSchoolStudent))
  print("Mode of the UG students math score is "+ str(mode_UGStudent))
  
  print("standard deviation of PG student dataset is "+ str(std_HighSchoolStudent))
  print("standard deviation of the High school student dataset is "+ str(std_HighSchoolStudent))
  print("standard deviation of the UG student dataset is "+ str(std_UGStudent))
  
  print("{}% of PG student dataset lies within first standard deviation".format(len(data_within_first_std)* 100 / len(data)))
  print("{}% of PG stundent dataset lies within second standard deviation".format(len(data_within_second_std)*100/ len(data)))
  print("{}% of PG student dataset lies within the third standard deviation".format(len(data_within_third_std)*100 / len(data)))
  print("{}% of high school student dataset lies within the second standard deviation".format(len(data1_within_second_std)*100 / len(data1)))
  print("{}% of high school student dataset lies within the third standard deviation".format(len(data1_within_third_std)*100 / len(data1)))
  
  

 show_dataStats()

 def plotFigures():
      fig = ff.create_distplot([data], ['Maths score'], show_hist = False)
      fig.add_trace(go.Scatter(x=[Mean_HighSchoolStudent, Mean_HighSchoolStudent], y=[0, 0.1], mode="lines", name="MEAN"))
      fig.add_trace(go.Scatter(x =[first_std_PG_start, first_std_PG_start], y =[0, 0.1], mode ='lines', name ="STANDARD DEVATION 1"))
      fig.add_trace(go.Scatter(x = [first_std_PG_end, first_std_PG_end], y =[0, 0.1], mode ='lines', name = "STANDARD DEVATION 1"))
      fig.add_trace(go.Scatter(x =[second_std_PG_start, second_std_PG_start], y =[0, 0.1], mode = 'lines', name =" STANDARD DEVATION 2"))
      fig.add_trace(go.Scatter(x =[second_std_PG_end, second_std_PG_end], y =[0, 0.1], mode = 'lines', name =" STANDARD DEVATION 2"))
      fig.add_trace(go.Scatter(x =[third_std_PG_start, third_std_PG_start], y =[0, 0.1], mode = 'lines', name =" STANDARD DEVATION 3"))
      fig.add_trace(go.Scatter(x =[third_std_PG_end, third_std_PG_end], y =[0, 0.1], mode = 'lines', name =" STANDARD DEVATION 3"))
      fig.show()
       
      fig1 = ff.create_distplot([data1], ['Maths score'], show_hist = True)
      fig1.add_trace(go.Scatter(x=[Mean_HighSchoolStudent, Mean_HighSchoolStudent], y=[0, 0.1], mode="lines", name="MEAN"))
      fig1.add_trace(go.Scatter(x=[first_std_HG_start, first_std_HG_start], y=[0, 0.1], mode="lines", name="STANDARD DEVATION 1"))
      fig1.add_trace(go.Scatter(x=[first_std_HG_end, first_std_HG_end], y=[0, 0.1], mode="lines", name="STANDARD DEVATION 1"))
      fig1.add_trace(go.Scatter(x=[second_std_HG_start, second_std_HG_start], y=[0, 0.1], mode="lines", name="STANDARD DEVATION 2"))
      fig1.add_trace(go.Scatter(x=[second_std_HG_end, second_std_HG_end], y=[0, 0.1], mode="lines", name="STANDARD DEVATION 2"))
      fig1.add_trace(go.Scatter(x=[third_std_HG_start, third_std_HG_start], y=[0, 0.1], mode="lines", name="STANDARD DEVATION 3"))
      fig1.add_trace(go.Scatter(x=[third_std_HG_end, third_std_HG_end], y=[0, 0.1], mode="lines", name="STANDARD DEVATION 3"))
      fig1.show()
 

 plotFigures()

setup()


       

     


       

