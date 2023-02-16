# -*- coding:utf-8 -*-
from analyzer import analyzer

pth=input("path:").strip()
run=analyzer(pth)
run.print_report()