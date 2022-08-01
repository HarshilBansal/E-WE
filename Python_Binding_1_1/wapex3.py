#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wap

server = 'http://api.wolframalpha.com/v2/query.jsp'
appid = 'XXXX'
input = 'pi'

waeo = wap.WolframAlphaEngine(appid, server)

queryStr = waeo.CreateQuery(input)
wap.WolframAlphaQuery(queryStr, appid)
result = waeo.PerformQuery(queryStr)
result = wap.WolframAlphaQueryResult(result)

for pod in result.Pods():
	waPod = wap.Pod(pod)
	title = "Pod.title: " + waPod.Title()[0]
	print title
	for subpod in waPod.Subpods():
		waSubpod = wap.Subpod(subpod)
		plaintext = waSubpod.Plaintext()[0]
		img = waSubpod.Img()
		src = wap.scanbranches(img[0], 'src')[0]
		alt = wap.scanbranches(img[0], 'alt')[0]
		print "-------------"
		print "img.src: " + src
		print "img.alt: " + alt
	print "\n"