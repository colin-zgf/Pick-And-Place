import json
import numpy as np
from plotly.graph_objs import Box
from plotly.offline import plot

# from IK import T_total

# compute the FK, then compute the errors
# FK_matrix = T_total.evalf(subs={q1: px, q2: py, q3: pz, q4: roll, q5: pitch, q6: yaw})

# how to jsonify numpy arrays https://stackoverflow.com/a/32850511
px_error_list = np.random.uniform(low = -0.1, high=0.1, size=50).tolist()
py_error_list = np.random.uniform(low = -0.1, high=0.1, size=50).tolist()
pz_error_list = np.random.uniform(low = -0.1, high=0.1, size=50).tolist()
roll_error_list = np.random.uniform(low = -0.1, high=0.1, size=50).tolist()
pitch_error_list = np.random.uniform(low = -0.1, high=0.1, size=50).tolist()
yaw_error_list = np.random.uniform(low = -0.1, high=0.1, size=50).tolist()

error_data = {
    "px": px_error_list,
    "py": py_error_list,
    "pz": pz_error_list,
    "roll": roll_error_list,
    "pitch": pitch_error_list,
    "yaw": yaw_error_list,
}

# save to disk
error_list_path = "./error_list.json"
# with open(error_list_path, "w") as error_list_file:
#     json_error_list = json.dump(error_data, error_list_file)

# open error list from disk
with open(error_list_path, "r") as error_list_file:
    json_error_list = json.loads(error_list_file.read())


px_error_list = json_error_list["px"]
py_error_list = json_error_list["py"]
pz_error_list = json_error_list["pz"]
roll_error_list = json_error_list["roll"]
pitch_error_list = json_error_list["pitch"]
yaw_error_list = json_error_list["yaw"]


# prepare the data for the box plot for plotly to plot
# box plot taken here https://plot.ly/python/box-plots/
px_errors = Box(x=1,
                y=px_error_list,
                name='px'
                )
py_errors = Box(
    x=2,
    y=py_error_list,
    name='py'

)
pz_errors = Box(
    x=3,
    y=pz_error_list,
    name='pz'

)
roll_errors = Box(
    x=4,
    y=roll_error_list,
    name='roll'

)
pitch_errors = Box(
    x=5,
    y=pitch_error_list,
    name='pitch'

)
yaw_errors = Box(
    x=6,
    y=yaw_error_list,
    name='yaw'
)
data = [px_errors, py_errors, pz_errors, roll_errors, pitch_errors, yaw_errors]
plot({"data": data})