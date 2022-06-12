from indeed import get_jobs as get_indeed_jobs
from save import save_to_csv

indeed_jobs = get_indeed_jobs()
save_to_csv(indeed_jobs)
