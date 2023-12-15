class NationalPark:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, "name") and isinstance(name, str) and len(name) >= 3:
            self._name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        best = self.visitors()[0]
        times = best.total_visits_at_park(self)

        for visitor in self.visitors():
            visited = visitor.total_visits_at_park(self)
            if visited > times:
                best = visitor
                times = visited

        return best


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.__class__.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if (
            isinstance(start_date, str)
            and len(start_date) >= 7
            and len(start_date.split(" ")) == 2
        ):
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if (
            isinstance(end_date, str)
            and len(end_date) >= 7
            and len(end_date.split(" ")) == 2
        ):
            self._end_date = end_date

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park


class Visitor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1, 16):
            self._name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]

    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))

    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park is park])
