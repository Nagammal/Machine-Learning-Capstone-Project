import pandas as pd
class Univariate():
    
    def quan_qual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtype=='O'):   
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual
    
    def descriptive_analysis(dataset, quan):
        descriptive_analysis_table = pd.DataFrame(index=[
            "Mean", "Median", "Mode", "Q1:25th", "Q2:50th", "Q3:75th", "Q:99th",
            "Q4:100th", "skewness", "kurtosis", "variance", "std_deviation"
        ], columns=quan)

        for columnName in quan:
            descriptive_analysis_table[columnName]["Mean"] = dataset[columnName].mean()
            descriptive_analysis_table[columnName]["Median"] = dataset[columnName].median()
            descriptive_analysis_table[columnName]["Mode"] = dataset[columnName].mode()[0]
            descriptive_analysis_table[columnName]["Q1:25th"] = dataset[columnName].quantile(0.25)
            descriptive_analysis_table[columnName]["Q2:50th"] = dataset[columnName].quantile(0.50)
            descriptive_analysis_table[columnName]["Q3:75th"] = dataset[columnName].quantile(0.75)
            descriptive_analysis_table[columnName]["Q:99th"] = dataset[columnName].quantile(0.99)
            descriptive_analysis_table[columnName]["Q4:100th"] = dataset[columnName].max()
            descriptive_analysis_table[columnName]["skewness"] = dataset[columnName].skew()
            descriptive_analysis_table[columnName]["kurtosis"] = dataset[columnName].kurtosis()
            descriptive_analysis_table[columnName]["variance"] = dataset[columnName].var()
            descriptive_analysis_table[columnName]["std_deviation"] = dataset[columnName].std()
            descriptive_analysis_table[columnName]["IQR"]=descriptive_analysis_table[columnName]["Q3:75th"] - descriptive_analysis_table[columnName]["Q1:25th"]
            descriptive_analysis_table[columnName]["1.5rule"]=1.5*descriptive_analysis_table[columnName]["IQR"]
            descriptive_analysis_table[columnName]["lesser_outlier"]=descriptive_analysis_table[columnName]["Q1:25th"]-descriptive_analysis_table[columnName]["1.5rule"]
            descriptive_analysis_table[columnName]["greater_outlier"]=  descriptive_analysis_table[columnName]["Q3:75th"]+descriptive_analysis_table[columnName]["1.5rule"]
            descriptive_analysis_table[columnName]["min"]=dataset[columnName].min()
            descriptive_analysis_table[columnName]["max"]=dataset[columnName].max()

        return descriptive_analysis_table