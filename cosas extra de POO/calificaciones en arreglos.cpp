#include <iostream>
#include <string>

using namespace std;

int main() {
    string alumno;
    int asistenciasTotales, asistenciasAlumno;
    double participaciones, trabajos, reportes, examen;

    cin >> alumno;
    cin >> asistenciasTotales;
    cin >> asistenciasAlumno;
    cin >> examen;
    cin >> reportes;
    cin >> trabajos;
    cin >> participaciones;

    double porcentajeAsistencia = ((double)asistenciasAlumno / asistenciasTotales) * 100;

    bool cumpleAsistencia = (porcentajeAsistencia >= 80.0);
    bool cumpleExamen = (examen >= 5.0);

    double notaAsistencia = (porcentajeAsistencia / 10.0);
    double notaReporteAsistencia = (reportes + notaAsistencia) / 2.0;
    double notaTrabajoParticipacion = (trabajos + participaciones) / 2.0;

    double notaFinal = (examen * 0.40) + (notaReporteAsistencia * 0.30) + (notaTrabajoParticipacion * 0.30);

    cout << alumno << "\n";
    cout << porcentajeAsistencia << "%\n";
    cout << notaFinal << "\n";

    if (cumpleAsistencia && cumpleExamen && notaFinal >= 6.0) {
        cout << "APROBADO\n";
    } else {
        cout << "REPROBADO\n";
    }

    return 0;
}