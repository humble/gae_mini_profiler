from webapp2 import WSGIApplication

from gae_mini_profiler import profiler

app = WSGIApplication([
    ("/gae_mini_profiler/request", profiler.RequestStatsHandler),
    ("/gae_mini_profiler/shared", profiler.SharedStatsHandler),
])
