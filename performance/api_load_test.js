import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    vus: 10,        // 10 virtuella användare
    duration: '10s' // kör i 10 sekunder
};

export default function () {
    const res = http.get('https://souderbroder-loan-lab.lovable.app/partner-loan-api');

    check(res, {
        'status is 200': (r) => r.status === 200,
    });

    sleep(1);
}
