import pandas as pd

def load_and_process(path):
    
    averageWeeks = 52.1429 # average weeks in a year
    dn = pd.read_csv(path)
    dn = (
        pd.DataFrame(dn)
       .drop(columns=['cg','cl','E-N'])
      # .insert(loc = 0, column='Average-Hourly', value =round(dn['Salary'] / (dn['Hours-per-week']*averageWeeks)))       
    )
    dn['Average-Hourly'] = round((dn['Salary'] / (dn['Hours-per-week']*averageWeeks)),2)

    return dn