import SimpleITK as sitk
import csv

# <demo> auto

# Load the Images to be measured
ScalarValuesFile = '~/SimpleITK-MICCAI-2011-Tutorial/Data/FA.png'
ScalarValuesImage = sitk.Cast( sitk.ReadImage(ScalarValuesFile), sitk.sitkUInt32 )
sitk.Show ( ScalarValuesImage )

LabelMapFile = '~/SimpleITK-MICCAI-2011-Tutorial/Data/LB.png'
LabelMapImage = sitk.Cast( sitk.ReadImage(LabelMapFile), sitk.sitkUInt32 )
sitk.Show ( LabelMapFile )

# <demo> stop

lsfilter = sitk.LabelStatisticsImageFilter()
lsfilter.Execute(LabelMapImage,ScalarValuesImage)
keys = lsfilter.GetValidLabels();

# <demo> stop

### Now extract measurement values to cataloging in a database/spreadsheet
MySubjectID="Subj01"
measurementDict=dict()
for labelValue in keys:
  uniqueId = ( MySubjectID, labelValue )
  measurementMap=lsfilter.GetMeasurementMap(labelValue)
  measurementDict[uniqueId]=dict( measurementMap )

# <demo> stop

print("DUMPING MEASUREMENT DICTIONARY")
print(measurementDict)
#A map between internal labels and header row strings.
headerMap={'SUBJID':'SubjectID',
           'LABELID':'LabelID',
           'Variance':'Variance',
           'Minimum':'Minimum',
           'Maximum':'Maximum',
           'Mean':'Mean',
           'Count':'NumPixels',
           'approxMedian':'Median',
           'Sum':'Sum',
           'Sigma':'Sigma'}

# <demo> stop

csvFileName="MyValues.csv"
csvFile=open(csvFileName, 'wb')
myDictWriter=csv.DictWriter(csvFile,headerMap.keys())
myDictWriter.writerow(headerMap)
for uniqueId in measurementDict.keys():
  unrollRow = measurementDict[uniqueId]
  unrollRow['SUBJID']=uniqueId[0]
  unrollRow['LABELID']=uniqueId[1]
  myDictWriter.writerow(unrollRow)

csvFile.close()
