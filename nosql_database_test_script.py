from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from credentials import USERNAME, PASSWORD

cloud_config= {
        'secure_connect_bundle': 'assets/secure-connect-hackwestern-chaotic-incarnate.zip'
}
auth_provider = PlainTextAuthProvider(USERNAME, PASSWORD)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")