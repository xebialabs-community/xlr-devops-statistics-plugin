#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from com.xebialabs.xlrelease.api.v1.forms import DeliveryFilters, DeliveryOrderMode

if deliveryScope == "ALL":
    deliveryScope = ["IN_PROGRESS", "COMPLETED"]
else:
    deliveryScope = [deliveryScope]

# Create filter
deliveryFilters = DeliveryFilters()
statusStrings = [str(status) for status in deliveryFilters.getStatuses()]
statusIndexes = [statusStrings.index(status) for status in deliveryScope]
statusFilter = []
for statusIndex in statusIndexes:
    statusFilter.append(deliveryFilters.getStatuses()[statusIndex])

deliveryFilters.statuses = statusFilter

deliveryPoints = []
pageSizes = [min(maxDeliveriesCount - i, 100) for i in range(0, maxDeliveriesCount, 100)]
for page in range(len(pageSizes)):
    deliveries = _deliveryApi.searchDeliveries(deliveryFilters, page, pageSizes[page], DeliveryOrderMode.valueOf(deliveryOrderMode))
    for delivery in deliveries:
        deliveryPoints.append(
            [
                delivery.title,
                str(len(delivery.releaseIds)),
                str(len(delivery.trackedItems)),
                str(delivery.status).replace('_',' '),
                str(delivery.startDate),
                str(delivery.endDate),
                delivery.id
            ]
        )

inProgressPoints = [delivery for delivery in deliveryPoints if str(delivery[3]) == "IN PROGRESS"]
completedPoints = [delivery for delivery in deliveryPoints if str(delivery[3]) == "COMPLETED"]

data = {
    "deliveryPoints": deliveryPoints,
    "inProgressPoints": inProgressPoints,
    "completedPoints": completedPoints
}