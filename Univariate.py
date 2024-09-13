import pandas as pd
class Univariate():
    def quanQual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset.columns:
            if(dataset[columnName].dtypes=='O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return qual,quan
    def freqTable(columnName, dataset):
        # Create a new dictionary to store the frequency table
        freq_table = {}

        # Assign unique values and their frequencies to the dictionary
        freq_table["uniq_values"] = dataset[columnName].value_counts().index
        freq_table["Frequency"] = dataset[columnName].value_counts().values
        freq_table["Relative_frequency"] = freq_table["Frequency"] / len(dataset)
        freq_table["cumsum"] = freq_table["Relative_frequency"].cumsum()

        # Convert the dictionary to a DataFrame if needed
        freq_table_df = pd.DataFrame(freq_table)

        return freq_table_df
       def univariate(dataset,quan):

            descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5Rule",
                                    "lesser","greater","min","max","var","std"],columns=quan)
            for columnName in quan:
                descriptive[columnName]["Mean"]=dataset[columnName].mean()
                descriptive[columnName]["Median"]=dataset[columnName].median()
                descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
                descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
                descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
                descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
                descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
                descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
                descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
                descriptive[columnName]["1.5Rule"]=1.5*descriptive[columnName]["IQR"]
                descriptive[columnName]["lesser"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5Rule"]
                descriptive[columnName]["greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5Rule"]
                descriptive[columnName]["min"]=dataset[columnName].min()
                descriptive[columnName]["max"]=dataset[columnName].max()
                descriptive[columnName]["var"]=dataset[columnName].var()
                descriptive[columnName]["std"]=dataset[columnName].std()
            return descriptive
    def lesser_greater(lesser,greater,quan):
        
        lesser=[]
        greater=[]
        for columnName in quan:
            if(descriptive[columnName]["min"]<descriptive[columnName]["lesser"]):
                lesser.append(columnName)
            if(descriptive[columnName]["max"]>descriptive[columnName]["greater"]):
                greater.append(columnName)
        return lesser,greater
    
    def Replace(descriptive):
        for columnName in lesser:

            dataset[columnName][dataset[columnName]<descriptive[columnName]["lesser"]]=descriptive[columnName]["lesser"]
        for columnName in greater:
            dataset[columnName][dataset[columnName]>descriptive[columnName]["greater"]]=descriptive[columnName]["greater"]
        return descriptive
