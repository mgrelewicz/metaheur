# metaheur

The Uncapacitated Facility Location Problem (UFLP)
deals with finding a subset of facilities from a given set of potential facility locations to meet the demands of all the customers such that the sum of the opening cost for each of the opened facilities and the service cost (or connection cost) is minimized

Solution proposal:
1) declare how many client_locations should be serviced by one facility
2) choose first facility_location (randomly)
3) search for group of clients with minimal sum of distances to chosen facility
4) search for client with maximum distance to chosen facility
5) set next location of facility which is closest to client found in point 4)
6) repeat points 2-5 for other locations
