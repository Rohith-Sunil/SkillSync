import pandas as pd
import spacy
from func import create_profile, plot_df
from constants import DATA_PATH, SKILL_FILE_PATH
from init_parser import init_parser_func
from tqdm import tqdm

nlp = spacy.load('en_core_web_sm')


if __name__ == '__main__':
	
	matcher = init_parser_func(nlp, SKILL_FILE_PATH, file_type="excel")
	
	final_database = pd.DataFrame()
	df = pd.read_excel(DATA_PATH)
	

	for each in tqdm(range(len(df))):

		text = df.loc[each,'Text']
		application_subject = df.loc[each,'Company']
		data = create_profile(nlp,matcher,text,application_subject)
		final_database = pd.concat([final_database, data], ignore_index=True)



	final_database.to_csv('../output/Data.csv', index=False)

	plot_df(final_database)
 




