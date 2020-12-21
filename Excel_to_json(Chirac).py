
import pandas

excel_data_df = pandas.read_excel('data/data_jacque chirac/jacque chirac_Twitter.xlsx', sheet_name='Posts')

twitter_json = excel_data_df.to_json(path_or_buf='data/data_jacque chirac/jacque chirac_Twitter.json')

excel_data_df = pandas.read_excel('data/data_jacque chirac/jacque chirac_Instagram.xlsx', sheet_name='Caption')

Instagram_json = excel_data_df.to_json(path_or_buf='data/data_jacque chirac/jacque chirac_Instagram.xlsx.json')