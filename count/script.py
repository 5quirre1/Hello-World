import os
import requests

repo_folder = './'
API_URL = 'https://code-lang-api.vercel.app/api/language'

def get_language_from_extension(file_extension):
    response = requests.get(f'{API_URL}/{file_extension}')
    if response.status_code == 200:
        data = response.json()
        if 'language' in data:
            return data['language']
    return 'Unknown'

def count_files_by_language():
    file_count = 0
    language_counts = {}

    for root, _, files in os.walk(repo_folder):
        for file in files:
            file_count += 1
            file_extension = file.split('.')[-1].lower()
            language = get_language_from_extension(file_extension)

            if language in language_counts:
                language_counts[language] += 1
            else:
                language_counts[language] = 1

    return file_count, language_counts

total_files, language_files = count_files_by_language()

readme_content = f"**File count: {total_files}**\n\n"
for language, count in language_files.items():
    readme_content += f"{language}: {count}\n"

print(readme_content)
