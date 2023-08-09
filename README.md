# Metriq API client

This is a client for [Metriq](https://metriq.info) read/write API.

It is adapted from the [PapersWithCode client](https://github.com/paperswithcode/paperswithcode-client), with thanks!

The API is completely covered by the client and it wraps all the API models
into python objects and communicates with the API by getting and passing those
objects from and to the api client.

## Quick usage example

You will require the [`pipenv` package](https://pipenv.pypa.io/en/latest/) on your machine in order to instantiate a 
virtual environment. This can be done with `pip install --user pipenv`.

You will then need to install and activate the virtual environment:

```bash
pipenv install
pipenv shell
```

Once the virtual environment has been activated, to check that the `metriq-client` API is working as expected, run the 
following example script from `metriq-client/examples/metriq_hello.py`:

```python
from metriq import MetriqClient

client = MetriqClient(token="[Get this token from your web app account, and replace this string with it.]")
print(client.hello())
>>> {'status': 'API is working', 'message': 'This is the Metriq public REST API.'}
```

## Further usage
### Submissions
Many details of submissions can be managed using the client. For example, the following functionalities can be invoked:
- Adding a submission or any part of one (method, tag, task, etc.) with `submission_add` and related functions.
- Deleting a submission with `submission_delete`.
- Sorting submissions (by latest, popular, or trending) with `submission_get_by_*`.
- Upvoting a submission with `submission_upvote`.
- Updating a submission with `submission_update`.

### Platforms
Information on platforms can also be accessed and edited: 
- Platforms can be added with `platform_add` and updated with `platform_update`.
- A list of platforms can be invoked using `platform_get`.
- A list of platforms on sorted by how many submission each has using `platform_get_submission_count`.

### Tags
Similarly, with the client, it is possible to get tag information from Metriq. This includes being able to get a list of tag items with `tag_get`, or a list of their names with `tag_get_names`.

### Tasks
The client can also:
- Add tasks with `task_add`.
- Update taskswith `task_update`.
- Get information on tasks with `task_get` and `task_get_*`.

### Methods
Functions exist for accessing information about methods:
- Adding a method to Metriq with `method_add`.
- Returning infomration about methods with `method_get` and `method_get_*`.
- Updating a method with `method_update`.

For even more examples of usage, consult `metriq-client/examples`.
