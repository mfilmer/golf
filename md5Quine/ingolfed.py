P='''import md5
a=md5.new("P=''"+"'"+P+"''"+"'\n"+P)
print a.hexdigest()'''
import md5
a=md5.new("P=''"+"'"+P+"''"+"'\\n"+P)
print a.hexdigest()