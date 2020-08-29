//mapreduce
db.runCommand(
	{
		mapreduce:"power_test"
		,map : function () {
	emit(this.BYQJH , {SJSJ: this.SJSJ, YGGL: this.YGGL})
}
		,reduce : function (key,values) {
	var ret = {date_power :[]};
	values.forEach(function(val){
		if(val.SJSJ != null&&val.YGGL !=null){
		ret.date_power.push({SJSJ: val.SJSJ, YGGL: val.YGGL}})
	return ret;
}
		,out : "power_test_new"
	}
	)

//,sort :{BYQJH : 1}
//NumLong to String XXXX NO!
db.testMR_result.find().forEach(

	function(item){
		var v = item._id + "";
		item._id = v.toString();
		db.testMR_result.save(item);
	}
	)

//find
db.testMR_result.findOne({'_id':NumberLong(5113001602)})


//CSV
mongoimport --db jxpower --collection power_1800 --type csv --headerline --ignoreBlanks --file /mnt/hgfs/LinuxSharedData/SK_DATA_SSLSD_2018_0.csv

//


//mapreduce version2.0
db.runCommand(
	{
		mapreduce:"power_1800_0"
		,map : function () {
	emit(this.BYQJH , {SJSJ: this.SJSJ, YGGL: this.YGGL})
}
		,reduce : function (key,values) {
	var ret = {date_power :[]};
	values.forEach(function(val){
		if(val.SJSJ != null&&val.YGGL !=null){
			ret.date_power.push({SJSJ: val.SJSJ, YGGL: val.YGGL});
		}
	})
	return ret;
}
		,out : "power_1800_0_n2"
		,sort : {BYQJH:1}
	}
	);


 db.power_1800_0_n2.find({_id:{$exists:true}}).forEach(function(x){
	x._id = x._id*1000;
	db.power_1800_0_n2.save(x);
})


.forEach(function(x){
	x._id = x._id/1000;
	db.power_1800_0_n2.save(x);
})

{_id:{$exists:true}}.forEach(function(x){
	x._id = x._id*1000
	db.power_1800_0_n2.save(x)
})


//mapreduce version3.0

db.runCommand(
	{
		mapreduce:"power_test"
		,map : function () {
		var i = this.BYQJH.toNumber();
	emit(i.toString(), {SJSJ: this.SJSJ, YGGL: this.YGGL})
}
		,reduce : function (key,values) {
	var ret = {date_power :[]};
	values.forEach(function(val){
		//if(val.SJSJ != null&&val.YGGL !=null){
			ret.date_power.push({SJSJ: val.SJSJ, YGGL: val.YGGL});
		//}
	})
	return ret;
}
		,out : "power_test_2"
		//,sort : {BYQJH:1}
	}
	);


"BH,SJSJ,PTBB,CTBB,JSSJ,AXDL,BXDL,CXDL,AXDY,BXDY,CXDY,YGGL,WGGL,GLYS,AXYGGL,BXYGGL,CXYGGL,AXWGGL,BXWGGL,CXWGGL,ZDLJDZ,LXDL,AXDYJBL,BXDYJBL,CXDYJBL,BYQJH.string()"




//4.0
db.runCommand(
	{
		mapreduce:"power_8"
		,map : function () {
	emit(this.BYQJH, {SJSJ: this.SJSJ, YGGL: this.YGGL})
}
		,reduce : function (key,values) {
	var ret = {date_power :[]};
	values.forEach(function(val){
		if(val.SJSJ != null&&val.YGGL !=null){
			ret.date_power.push({SJSJ: val.SJSJ, YGGL: val.YGGL});
		}
	})
	return ret;
}
		,out : "power_result_test3"
		,sort : {BYQJH:1}
	}
	);



db.runCommand(
	{
		mapreduce:"power_8"
		,map : function () {
	emit(this.BYQJH, {SJSJ: this.SJSJ, YGGL: this.YGGL})
}
		,reduce : function (key,values) {
	var ret = {date_power :[]};
	values.forEach(function(val){
			ret.date_power.push({SJSJ: val.SJSJ, YGGL: val.YGGL});
	})
	return ret;
}
		,out : "power_result_test2"
	}
	);




db.power_8.remove({"SJSJ":{"$in":[null],"$exists":true}})
db.power_8.remove({"SJSJ":null})

db.db17_8.aggregate([
	{$sort:{"SJSJ":1}},
	{"$group":{
		_id :"$BYQJH",
		data :{ $push :{ SJSJ:"$SJSJ", YGGL:"$YGGL"}},
		count :{"$sum":1}
	}},
	{$match :{"count":{"$gt":1}}},
	{$out: "Aggr_result"}
	],
	{
		allowDiskUse: true
	}
	);



mongoimport -h 192.168.122.87 --port 27017 --db jxdb --collection db17_8 --type csv -f "BYQJH,unknown,SJSJ,AXDY,BXDY,CXDY,AXDL,BXDL,CXDL,YGGL,AXYGGL,BXYGGL,CXYGGL,WGGL,AXWGGL,BXWGGL,CXWGGL" --ignoreBlanks --file I:\江西电网数据\2017\2017-08-30.csv

-h 192.168.122.87 --port 27017

mongoimport --db jxdb --collection db17_7 --type csv -f "BYQJH,unknown,SJSJ,AXDY,BXDY,CXDY,AXDL,BXDL,CXDL,YGGL,AXYGGL,BXYGGL,CXYGGL,WGGL,AXWGGL,BXWGGL,CXWGGL" --ignoreBlanks --file /state/2017/2017-07-01.csv
