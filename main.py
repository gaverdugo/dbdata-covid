import pandas as pd

def main():
  csv_df = pd.read_csv('casos-diarios.csv')
  states_info_df = pd.DataFrame(pd.concat([csv_df['cve_ent'], csv_df['poblacion'], csv_df['nombre']], axis=1))
  cases_df = csv_df.drop(csv_df.columns[[0,1,2]], axis=1)
  states_ids = list(states_info_df['cve_ent'])
  cases_list = []

  for (column_name, column_data) in cases_df.iteritems():
    cases_day = [{"state_id": states_ids[i], "cases": column_data[i], "date": column_name} for i in range(0, len(states_ids))]
    cases_list = cases_list + cases_day

  ordered_cases_df = pd.DataFrame(cases_list)

  states_info_df.to_csv('states.csv', index=False)
  ordered_cases_df.to_csv('cases.csv', index=False)


if __name__ == "__main__":
  main()