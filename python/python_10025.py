# Getting request param from url
&gt;&gt;&gt; from urlparse import parse_qs
&gt;&gt;&gt; parse_qs('next=/contact/200/10626096&amp;back%3DZHViYWkuZHViaXp6bGUubmxoL2NsYXNzaWZpZWQvYXV0b3M0eDRzL2FjdXJhL2NzeGVsLz95ZWFyX19ndGU9JmFkZGVkX19ndGU9JnNlbGxlcl90eXBlPSZpc19zZWFyY2g9MSZraWxvbWV0ZXJzX19ndGU9JnByaWNlX19ndGU9JnBsYWNlc19faWRfX2luPUVudGVyK0xvY2F0aW9uJTI4cyUyOStIZXJlJnBsYWNlc19faWRfX2luPSZ5ZWFyX19sdGU9MjAxMiZraWxvbWV0ZXJzX19sdGU9JmtleXdvcmRzPSZpc19iYXNpY19zZWFyY2hfd2lkZ2V0PTAmcHJpY2VfX2x0ZT0%3D')
{'next': ['/contact/200/10626096']}
