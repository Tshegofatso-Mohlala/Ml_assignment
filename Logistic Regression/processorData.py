import numpy as np

class processor:
    
    def __init__(self,data):
        self.data = data
        
    def Class(self,clss):
        class_num = None
        if(clss == 'no-recurrence-events'):
            class_num = 0
        if(clss == 'recurrence-events'):
            class_num = 1
        return class_num
    
    def age(self,age):
        age_num = None
        if (age == '10-19'):
            age_num = 1
        if (age == '20-29'):
            age_num = 2
        if (age == '30-39'):
            age_num = 3
        if (age == '40-49'):
            age_num = 4
        if (age == '50-59'):
            age_num = 5
        if (age == '60-69'):
            age_num = 6
        if (age == '70-79'):
            age_num = 7
        if (age == '80-89'):
            age_num = 8
        if (age == '90-99'):
            age_num = 9
        return age_num
    
    def menupause(self,menupause):
        menupause_num = None
        if (menupause == 'lt40'):
            menupause_num = 1
        if (menupause == 'ge40'):
            menupause_num = 2
        if (menupause == 'premeno'):
            menupause_num = 3
        return menupause_num
    
    def tumorSize(self,tumorSize):
        tumorSize_num = None
        if(tumorSize == '0-4'):
            tumorSize_num = 1
        if(tumorSize == '5-9'):
            tumorSize_num = 2
        if(tumorSize == '10-14'):
            tumorSize_num = 3
        if(tumorSize == '15-19'):
            tumorSize_num = 4
        if(tumorSize == '20-24'):
            tumorSize_num = 5
        if(tumorSize == '25-29'):
            tumorSize_num = 6
        if(tumorSize == '30-34'):
            tumorSize_num = 7
        if(tumorSize == '35-39'):
            tumorSize_num = 8
        if(tumorSize == '40-44'):
            tumorSize_num = 9
        if(tumorSize == '45-49'):
            tumorSize_num = 10
        if(tumorSize == '50-54'):
            tumorSize_num = 11
        if(tumorSize == '55-59'):
            tumorSize_num = 12
        return tumorSize_num
    
    def invNodes(self,inv_nodes):
        inv_nodes_num = None
        if(inv_nodes == '0-2'):
            inv_nodes_num = 1
        if(inv_nodes == '3-5'):
            inv_nodes_num = 2
        if(inv_nodes == '6-8'):
            inv_nodes_num = 3
        if(inv_nodes == '9-11'):
            inv_nodes_num = 4
        if(inv_nodes == '12-14'):
            inv_nodes_num = 5
        if(inv_nodes == '15-17'):
            inv_nodes_num = 6
        if(inv_nodes == '18-20'):
            inv_nodes_num = 7
        if(inv_nodes == '21-23'):
            inv_nodes_num = 8
        if(inv_nodes == '24-26'):
            inv_nodes_num = 9
        if(inv_nodes == '27-29'):
            inv_nodes_num = 10
        if(inv_nodes == '30-32'):
            inv_nodes_num = 11
        if(inv_nodes == '33-35'):
            inv_nodes_num = 12
        if(inv_nodes == '36-39'):
            inv_nodes_num = 13
        return inv_nodes_num
    
    def nodeCaps(self,node_caps):
        node_caps_num = None
        if(node_caps == 'yes'):
            node_caps_num = 1
        if(node_caps == 'no'):
            node_caps_num = 2
        return node_caps_num
    
    def degMalig(self,deg_malig):
        deg_malig_num = None
        if(deg_malig == '1'):
            deg_malig_num = 1
        if(deg_malig == '2'):
            deg_malig_num = 2
        if(deg_malig == '3'):
            deg_malig_num = 3
        return deg_malig_num
    
    def breast(self,breast):
        breast_num = None
        if(breast == 'left'):
            breast_num = 1
        if(breast == 'right'):
            breast_num = 2
        return breast_num
    
    def breastQuad(self,breast_quad):
        breast_quad_num = None
        if (breast_quad == 'left_low'):
            breast_quad_num = 1
        if (breast_quad == 'left_up'):
            breast_quad_num = 2
        if (breast_quad == 'right_low'):
            breast_quad_num = 3
        if(breast_quad == 'right_up'):
            breast_quad_num = 4
        if(breast_quad == 'central'):
            breast_quad_num = 5
        return breast_quad_num
    
    def irradiat(self,irradiat):
        irradiat_num = None
        if (irradiat == 'yes'):
            irradiat_num = 1
        if (irradiat == 'no'):
            irradiat_num = 2
        return irradiat_num
    
    def processedData(self):
        data = self.data
        processedData = []
        Data = []
        for i in range(0,len(data)):
            Data.append(self.Class(data[i][0]))
            Data.append(self.age(data[i][1]))
            Data.append(self.menupause(data[i][2]))
            Data.append(self.tumorSize(data[i][3]))
            Data.append(self.invNodes(data[i][4]))
            Data.append(self.nodeCaps(data[i][5]))
            Data.append(self.degMalig(data[i][6]))
            Data.append(self.breast(data[i][7]))
            Data.append(self.breastQuad(data[i][8]))
            Data.append(self.irradiat(data[i][9]))
            processedData.append(Data)
            Data = []
        return processedData
    
    def normalizedData(self):
        data = self.processedData();
        normalizedData = []
        for i in data:
            meanPerRow = np.mean(i[1:]) # exclude the class
            newData = (i[1:] - np.mean(i[1:])).tolist() # normalize the data and exclude the class
            newData.insert(0,i[0])
            normalizedData.append(newData)
        return normalizedData
            